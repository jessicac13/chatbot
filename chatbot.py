import re, json
from errbot import BotPlugin, botcmd, arg_botcmd, webhook, re_botcmd, ONLINE, AWAY


class Comandos(BotPlugin):
    """
    Comandos da Julinha Marvi·e.
    """

    def help
    
    @re_botcmd(pattern=r"(.| )+")
    def enviar_rota(self, msg, match):
        """
        Manda a Julinha seguir rota para o endereço X.
        """
        rota = str(match.group())
        
        mensagem = {}
        mensagem['rota'] = rota
        print(json.dumps(mensagem))
        # Envia "local" para o servidor de rotas, e fica esperando uma resposta.
        #
        # Quando chegar a resposta, formatar para o usuário final.
        yield("Siga-me até " + rota + ". Obrigada.:relaxed:")


#funções

    @re_botcmd(pattern=r"andar [0-9]+")
    def andar(self, msg, match):
        """
        Manda a Julinha andar x.
        """
        mensagem = {}
        mensagem['comando'] = "andar"
        quantidade = match.group().split(' ')[1]
        if quantidade:
            mensagem['valor'] = quantidade
            yield(mensagem)

    @botcmd
    def buzinar(self, msg, args):
        """
        Aciona a buzina do Arduino.
        """
        yield("Bip bip!:mega:")

    @botcmd
    def desligar(self, msg, args):
        """
        Desliga a Julinha.
        """
        yield("Foi um prazer trabalhar hoje! Beijo, me liga!:kissing_heart:")
        self.change_presence(AWAY)

    @botcmd
    def direita(self, msg, args):
        """
        Manda a Julinha virar à direita.
        """
        yield("Virando à direita!")

    @botcmd
    def esquerda(self, msg, args):
        """
        Manda a Julinha virar à esquerda.
        """
        yield("Virando à esquerda!")
    
    @botcmd
    def frente(self, msg, args):
        """
        Manda a Julinha ir à frente.
        """
        yield("Para frente e avante!")

    @botcmd
    def ligar(self, msg, args):
        """
        Liga a Julinha.
        """
        yield("Julinha às suas ordens, capitão!")
        self.change_presence(ONLINE)
      
    @botcmd
    def sirene(self, msg, args):
        """
        Aciona a sirene do Arduino.
        """
        yield("Uiuuu uiuuu!:rotating_light:")

    @botcmd
    def tras(self, msg, args):
        """
        Manda a Julinha para trás.
        """
        yield("Dando ré!")
