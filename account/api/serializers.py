from rest_framework import serializers
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    confirm_pass = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['email','username','password','confirm_pass']
        extra_kwargs = {
                    'password':{'write_only': True}
        }



        def save(self):
            account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    
            )
            password = self.validated_data['password']
            confirm_pass = self.validated_data['confirm_pass']

            if password != confirm_pass:
                raise serializers.ValidationError({'password':"Passwords don't match!"})
            account.set_password(password)
            account.save()

            return account