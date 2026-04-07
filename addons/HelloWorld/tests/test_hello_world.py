# El __init__.py principal del módulo NO debe importar la carpeta tests. Odoo la carga de forma independiente.
from odoo.tests.common import TransactionCase # type: ignore
from odoo.tests import tagged # type: ignore

@tagged('post_install', '-at_install', 'HelloWorld')
class TestHelloWorld(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # El setUpClass se ejecuta una vez para preparar los datos
        super(TestHelloWorld, cls).setUpClass()
        # Creamos un usuario de prueba o usamos el admin
        cls.record = cls.env['sh.hello.world'].create({
            'name': 'Test de Integración',
            'user_phrase': 'Hola desde el Test'
        })

    def test_01_initial_state(self):
        """Verificar que el estado inicial sea borrador"""
        self.assertEqual(self.record.state, 'draft', "El estado inicial debería ser 'draft'")

    def test_02_action_lock(self):
        """Probar que el botón de bloquear funciona"""
        self.record.action_lock()
        self.assertEqual(self.record.state, 'locked', "El estado debería cambiar a 'locked'")