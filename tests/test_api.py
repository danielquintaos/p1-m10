import unittest
from fastapi.testclient import TestClient
from api.main import app

class PedidoAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the FastAPI application."""
        self.client = TestClient(app)

    def test_get_root(self):
        """Test the root endpoint."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the Pedido API powered by FastAPI"})

    def test_list_pedidos(self):
        """Test the list pedidos endpoint."""
        response = self.client.get("/pedidos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_pedido(self):
        """Test creating a new pedido."""
        new_pedido = {'title': 'novo pedido', 'description': 'A new pedido description'}
        response = self.client.post("/novo", json=new_pedido)
        self.assertEqual(response.status_code, 201)
        self.assertIn('title', response.json())
        self.assertEqual(response.json()['title'], 'Novo pedido')

    def test_get_pedido(self):
        """Test retrieving a pedido by ID."""
        response = self.client.get("/pedidos/1")
        if response.status_code == 200:
            self.assertEqual(response.json()['id'], "1")
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_pedido(self):
        """Test updating an existing pedido."""
        updates = {'title': 'Updated pedido', 'description': 'Updated description'}
        response = self.client.put("/pedidos/1", json=updates)
        if response.status_code == 200:
            self.assertEqual(response.json()['title'], 'Updated pedido')
        else:
            self.assertEqual(response.status_code, 404)

    def test_delete_pedido(self):
        """Test deleting a pedido."""
        response = self.client.delete("/pedidos/1")
        if response.status_code == 204:
            # pedido was successfully deleted
            follow_up_response = self.client.get("/pedidos/1")
            self.assertEqual(follow_up_response.status_code, 404)
        else:
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
