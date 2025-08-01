import pytest

"""
Não é comum colocar os testes no mesmo arquivo que o código real. 
Para simplificar, os exemplos neste exercício têm código real no mesmo arquivo. 
Em projetos do Python do mundo real, os testes costumam ser separados por arquivos e 
diretórios do código que estão sendo testados.
"""

def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    if not isinstance(command, list):
        raise TypeError(f"É esperado 'command' do tipo list, mas foi recebido o tipo {type(command)}.")
    if sudo:
        return ["sudo"] + command
    return command


class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected

    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True)
        assert error.value.args[0] == "É esperado 'command' do tipo list, mas foi recebido o tipo <class 'str'>."
