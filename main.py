import requests
from bs4 import BeautifulSoup

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    return data

def consultar_ip(ip):
    url = f"https://ipinfo.io/{ip}/json/"
    response = requests.get(url)
    data = response.json()
    return data

def consultar_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    data = response.json()
    return data
def consultar_cpf(cpf):
    # URL do site para autenticação
    login_url = "https://mind-7.org/acesso/"
    cpf_url = f"https://mind-7.org/painel/consultas/cpf/consulta.php?cpf={cpf}"

    # Informações de autenticação
    login_payload = {
        "email": "miguelmarqs1233@gmail.com",
        "password": "Luis123@"
    }

    # Criar uma sessão para manter a autenticação
    with requests.Session() as session:
        # Fazer login
        session.post(login_url, data=login_payload)

        # Consultar CPF após o login
        response = session.get(cpf_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extrair informações da tabela
        tabela = soup.find("table", {"class": "customers"})

        # Verificar se a tabela foi encontrada antes de acessar seus elementos
        if tabela:
            dados = {}
            for row in tabela.find_all("tr"):
                colunas = row.find_all(["th", "td"])
                chave = colunas[0].text.strip()
                valor = colunas[1].text.strip()
                dados[chave] = valor

            return dados
        else:
            print("Tabela não encontrada. Verifique a página ou as alterações no código HTML.")
            return None

    # Criar uma sessão para manter a autenticação
    with requests.Session() as session:
        # Fazer login
        session.post(login_url, data=login_payload)

        # Consultar CPF após o login
        response = session.get(cpf_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extrair informações da tabela
        tabela = soup.find("table", {"class": "customers"})
        dados = {}
        for row in tabela.find_all("tr"):
            colunas = row.find_all(["th", "td"])
            chave = colunas[0].text.strip()
            valor = colunas[1].text.strip()
            dados[chave] = valor

        return dados

def exibir_menu():
    print("Menu:")
    print("1. Consultar CEP")
    print("2. Consultar IP")
    print("3. Consultar CNPJ")
    print("4. Consultar CPF")
    print("9. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cep = input("Digite o CEP que deseja consultar: ")
            resultado = consultar_cep(cep)
            print(resultado)
        elif opcao == "2":
            ip = input("Digite o IP que deseja consultar: ")
            resultado = consultar_ip(ip)
            print(resultado)
        elif opcao == "3":
            cnpj = input("Digite o CNPJ que deseja consultar: ")
            resultado = consultar_cnpj(cnpj)
            print(resultado)
        elif opcao == "4":  # Adicionando a opção de consultar CPF
            cpf = input("Digite o CPF que deseja consultar: ")
            resultado = consultar_cpf(cpf)
            # Imprima as informações desejadas do resultado
            print(f"Nome: {resultado.get('Nome', 'N/A')}")
            print(f"CPF: {resultado.get('CPF', 'N/A')}")
            print(f"Nascimento: {resultado.get('Nascimento', 'N/A')}")
            print(f"Nome da Mãe: {resultado.get('Nome da Mãe', 'N/A')}")
            # Adicione outras informações conforme necessário
            
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
