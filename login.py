from data import cadastros_dict
from token_repo import gerar_token_unico


def validar_login(input_name, input_password):
    """Alguma explicação do método

    Args:
        input_name (_type_): _description_
        input_password (_type_): _description_

    Returns:
        _type_: _description_
    """
    # If username or password are not informed, return right await
    if not input_name or not input_password:
        return
    # Finds a user
    db_user_dict = cadastros_dict.get(input_name.lower())
    # Checks if a user exists
    if not db_user_dict:
        return
    # Finds user password
    db_password = db_user_dict.get("senha")
    # Checks if password exists and matches
    if db_password and db_password == input_password:
        return db_user_dict


if __name__ == "__main__":
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        input_name = input("Digite seu nome: ")
        input_password = input("Digite sua senha: ")

        show_register = validar_login(input_name, input_password)

        if show_register:
            token = gerar_token_unico()
            print(f"Login bem-sucedido!\n{show_register}\nToken: {token}")
            break
        else:
            attempts += 1
            print("Nome ou senha incorretos!")

    if attempts == max_attempts:
        print(
            "Número máximo de tentativas atingido. Tente novamente mais tarde."
        )
