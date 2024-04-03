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


def test_update_user_200(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_404(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_200(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_404(client):
    response = client.delete('/users/0')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
