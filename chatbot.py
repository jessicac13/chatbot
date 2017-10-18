import re
from errbot import BotPlugin, botcmd, re_botcmd, ONLINE, AWAY


class ChatBot(BotPlugin):
    """
    Uma conversa franca com Julinho, o robô do Integrado.
    """

    @botcmd
    def descansar(self, msg, args):
        """
        Manda o Julinho descansar.
        """
        yield("Adeus, mundo cruel!")
        self.change_presence(AWAY, "Eu não estou aqui!")

    @botcmd
    def acordar(self, msg, args):
        """
        Manda o Julinho acordar.
        """
        yield("Sim, senhor SENHOR!")
        self.change_presence(ONLINE, "Às suas ordens!")

    @botcmd
    def buzinar(self, msg, args):
        """
        Aciona a buzina do Arduino.
        """
        yield("Bip bip!")

    @re_botcmd(pattern=r"andar [0-9]+")
    def andar(self, msg, match):
        """
        Aciona a buzina do Arduino.
        """
        mensagem = {}
        mensagem['comando'] = "andar"
        quantidade = match.group().split(' ')[0]
        if quantidade:
            mensagem['valor'] = quantidade
            yield(mensagem)
            
#batepapo


@botcmd
    def duvidei(self, msg, args):
        """
        Resposta Julinha à sua descrença.
        """
        yield("Duvidando? De mim? Que audácia!:rage:")

    @botcmd
    def like(self, msg, args):
        """
        Pede a Julinha um like.
        """
        yield(":thumbsup_all:")
    
    @re_botcmd(pattern=r"quer namorar comigo?")
    def namoro(self, msg, args):
        """
        Comando do rmayormartins.
        """
        yield("Se eu fosse real, talvez... :heart_eyes:")
    
    @re_botcmd(pattern=r"posso ganhar (uma|um) (bolacha|biscoito) por favor?")
    def biscoito_educado(self, msg, match):
        """
        Pede por um biscoito/bolacha para a Julinha, educadamente.
        """
        yield("Claro que sim, {}!").format(msg.frm)
        yield(":cookie:")

    @re_botcmd(pattern=r"quero (uma|um) (bolacha|biscoito)?")
    def biscoito(self, msg, match):
        """
        Pede por um biscoito/bolacha para a Julinha.
        """
        yield("Seja educado {}!").format(msg.frm)
    
    @re_botcmd(pattern=r"[cad(e|ê)|e] o (j|J)ulinho?")
    def julinho(self, msg, match):
        """
        Pergunta à Julinha sobre seu irmão.
        """
        yield("Está fazendo bip bip por aí...:robot_face:")
        yield("Mas você já procurou na portaria?")
        
