from direct.directbase.DirectStart import base

from otp.otpbase.OTPLocalizer import CustomSCStrings
from otp.speedchat.SCCustomTerminal import SCCustomTerminal
from otp.speedchat.SCMenu import SCMenu


class SCCustomMenu(SCMenu):

    def __init__(self):
        SCMenu.__init__(self)
        self.accept('customMessagesChanged', self.__customMessagesChanged)
        self.__customMessagesChanged()

    def destroy(self):
        SCMenu.destroy(self)

    def __customMessagesChanged(self):
        self.clearMenu()
        try:
            lt = base.localAvatar
        except:
            return

        for msgIndex in lt.customMessages:
            if CustomSCStrings.has_key(msgIndex):
                self.append(SCCustomTerminal(msgIndex))
