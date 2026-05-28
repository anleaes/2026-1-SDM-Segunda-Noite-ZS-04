document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('formRegistro');
    const senha = document.getElementById('id_senha');
    const confirmarSenha = document.getElementById('confirmar_senha');
    const erroSenha = document.getElementById('erro_senha');
    const tipoPerfil = document.getElementById('tipo_perfil');
    const secaoCidadao = document.getElementById('secao_cidadao');
    const secaoFuncionario = document.getElementById('secao_funcionario');
    const inputsCidadao = secaoCidadao.querySelectorAll('input, select');
    const inputsFuncionario = secaoFuncionario.querySelectorAll('input, select');

    function alternarPerfil(tipo) {
        if (tipo === 'cidadao') {
            secaoCidadao.style.display = 'block';
            secaoFuncionario.style.display = 'none';

            inputsCidadao.forEach(campo => campo.disabled = false);
            inputsFuncionario.forEach(campo => campo.disabled = true);
        } else {
            secaoCidadao.style.display = 'none';
            secaoFuncionario.style.display = 'block';

            inputsCidadao.forEach(campo => campo.disabled = true);
            inputsFuncionario.forEach(campo => campo.disabled = false);
        }
    };

    function verificarSenhasIguais() {
        if (senha.value === '' && confirmarSenha.value === '') {
            erroSenha.style.display = 'none';
            confirmarSenha.style.borderColor = '';
            return true;
        }

        if (confirmarSenha.value !== '') {
            if (senha.value !== confirmarSenha.value) {
                erroSenha.style.display = 'block';
                confirmarSenha.style.borderColor = 'red';
                return false;
            } else {
                erroSenha.style.display = 'none';
                confirmarSenha.style.borderColor = 'green';
                return true;
            }
        }
        return true;
    }

    senha.addEventListener('input', verificarSenhasIguais);
    confirmarSenha.addEventListener('input', verificarSenhasIguais);
    tipoPerfil.addEventListener('change', function() {
        alternarPerfil(this.value);
    });

    alternarPerfil(tipoPerfil.value);

    form.addEventListener('submit', function (event) {
        if (!verificarSenhasIguais() || senha.value !== confirmarSenha.value) {
            event.preventDefault();
            alert('Por favor, certifique-se de que as senhas são iguais.');
            confirmarSenha.focus();
        }
    });
});