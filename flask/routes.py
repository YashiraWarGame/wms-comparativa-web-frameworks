from flask import Flask, render_template, request, flash, session, redirect, url_for
from models import db, Ckanswertype, Pkchallenge, Pkanswer
from flask.ext.admin import Admin, BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from forms import IntroChallenge

# Configuraciones
app = Flask(__name__)
app.secret_key = "semilla"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/WMS'
db.init_app(app)

# Vistas
class IndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('index.html')

class TestChallengeView(BaseView):
    @expose('/', methods=('GET', 'POST'))
    def intro_challenge(self):
        form = IntroChallenge()
        if request.method == 'POST':
            if not form.validate():
                flash('Datos incorrectos')
                return self.render('intro-challenge.html', form=form)
            else:
                #valid = Pkchallenge.is_valid_answer('test2')
                valid = Pkchallenge.is_valid_answer(form.answer.data)
                message = 'Respuesta incorrecta'
                if valid:
                    message = 'Respuesta correcta'
                flash(message)
                return self.render('intro-challenge.html')
        elif request.method == 'GET':
            return self.render('intro-challenge.html', form=form)
        return self.render('intro-challenge.html', form=form)


admin = Admin(app, name="WMS", index_view=IndexView(name='Inicio'))
#admin.add_view(IndexView(name='Inicio'))

admin.add_view(TestChallengeView(name='Competir', endpoint='intro-challenge', category='Retos'))
admin.add_view(ModelView(Pkchallenge, db.session, name='Reto', endpoint='reto', category='Retos'))
admin.add_view(ModelView(Pkanswer, db.session, name='Respuesta', endpoint='respuesta', category='Respuestas'))
admin.add_view(ModelView(Ckanswertype, db.session, name='Tipo de Respuesta', endpoint='tipo-respuesta', category='Respuestas'))


@app.route('/')
def index():
    return redirect("/admin/")

if __name__ == '__main__':
    app.run(debug=True)