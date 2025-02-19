from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):#herança (flaskForm)
    username = StringField('Nome do Usuário', validators= [DataRequired(message='Este campo é obrigatório.')])
    email = StringField('E-mail', validators=[DataRequired(message='Este capo é obrigatório.'), Email(message='Por favor, insira um e-mail válido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Este capo é obrigatório.'), Length(6, 20, message='A senha deve ter entre 6 e 20 caracteres.')])
    confirmacao_senha =PasswordField('Confirmação da senha', validators=[DataRequired('Este campo é obrigatório.'), EqualTo('senha', message='As senhas devem ser iguais.')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):#tem que ser escrito assim validade_ para o flask conseguir rodar o validator
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça o login para continuar.')

class FormLogin(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(message='Este campo é obrigatório.'), Email(message='Por favor, insira um e-mail válido.')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Este campo é obrigatório.'), Length(6, 20 , message='A senha deve ter entre 6 e 20 caracteres.')])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', validators= [DataRequired(message='Este campo é obrigatório.')])
    email = StringField('E-mail', validators=[DataRequired(message='Este campo é obrigatório.'), Email(message='Por favor, insira um e-mail válido.')])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png'])])#lista de extensão que será permitido da foto
    
    curso_python = BooleanField('Python')
    curso_javascript = BooleanField ('JavaScript')
    curso_powerbi = BooleanField('Power BI')
    curso_java = BooleanField ('Java')
    curso_ruby = BooleanField ('Ruby')
    curso_sql = BooleanField ('SQL')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
              raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')

class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')