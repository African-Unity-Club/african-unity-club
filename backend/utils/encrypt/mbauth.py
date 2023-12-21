#!/usr/bin/env python3
"""
"""
import pyotp
from typing import Optional



class MobileGoogleAuth:

    # https://pypi.org/project/pyotp/

    # Cette URL peut ensuite être transformée en code QR 
    # (par exemple, à l'aide de https://github.com/soldair/node-qrcode), *
    # qui peut ensuite être scanné et ajouté à la liste des identifiants OTP de l'utilisateur.

    """
    Configurer Google Authenticator sur le côté client :

    Demandez à l'utilisateur de télécharger et d'installer l'application Google Authenticator sur son appareil mobile.
    Dans votre application, fournissez à l'utilisateur une interface pour activer l'authentification à deux facteurs.
    Générer une clé secrète pour chaque utilisateur sur le côté serveur :

    Lorsqu'un utilisateur active l'authentification à deux facteurs, générez une clé secrète pour cet utilisateur côté serveur.
    Stockez cette clé secrète de manière sécurisée associée à l'utilisateur dans votre base de données.
    Afficher la clé secrète à l'utilisateur :

    Affichez la clé secrète à l'utilisateur après l'activation de l'authentification à deux facteurs. 
    Cela peut être un code QR contenant l'URL TOTP ou simplement la clé secrète elle-même.
    Configurer Google Authenticator avec la clé secrète :

    L'utilisateur doit ajouter manuellement la clé secrète dans l'application Google Authenticator. 
    Cela peut se faire soit en scannant un code QR, soit en entrant la clé manuellement.
    Vérifier le code à usage unique lors de la connexion :

    Lorsque l'utilisateur se connecte, demandez le code à usage unique généré par Google Authenticator.
    Sur le côté serveur, utilisez la bibliothèque pyotp (ou une autre bibliothèque compatible) 
    pour vérifier si le code fourni par l'utilisateur correspond à celui généré à partir de la clé secrète stockée.
    """

    def __init__(self, appname: str, author: str):

        assert type(appname) is str, 'appname must be str'
        self.appname = appname

        assert type(author) is str, 'author must be str'
        self.author = author

    @property
    def keygen(self) -> str:

        return str(pyotp.random_base32())
    
    def qrcode(self, keygen: str):
        assert type(keygen) is str, 'keygen must be str'
        return pyotp.totp.TOTP(keygen).provisioning_uri(name=self.appname, issuer_name=self.author)

    def verify(self, keygen: str, usercode: str, ) -> bool:
        """
        codecskey = keygen
        """
        assert type(keygen) is str, 'keygen must be str'
        otp = pyotp.TOTP(keygen)
        
        assert type(usercode) is str, 'usercode must be str'
        return otp.verify(usercode)


MobileGoogleAuth = MobileGoogleAuth('AfricanUnityClub', 'MpiSoftware')
