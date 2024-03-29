def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'mau',
            'email': 'mau@teste.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'mau',
        'email': 'mau@teste.com',
    }


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'mau',
                'email': 'mau@teste.com',
            }
        ]
    }
