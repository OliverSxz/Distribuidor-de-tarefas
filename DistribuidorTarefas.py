from enum import Enum
from datetime import datetime


# ---------------- ENUMS ----------------

class Status(Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"


class Prioridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


# ---------------- MODELOS ----------------

class Tarefa:
    def __init__(self, titulo, prioridade):
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = Status.PENDENTE
        self.criada_em = datetime.now()

    def __str__(self):
        return f"{self.titulo} | {self.prioridade.name} | {self.status.value}"


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)


# ---------------- SISTEMA ----------------

class SistemaTarefas:
    def __init__(self):
        self.usuarios = []

    # -------- usuários --------
    def adicionar_usuario(self, nome):
        self.usuarios.append(Usuario(nome))
        print(f"Usuário '{nome}' criado com sucesso.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for u in self.usuarios:
            print(f"- {u.nome} ({len(u.tarefas)} tarefas)")

    def encontrar_usuario(self, nome):
        for u in self.usuarios:
            if u.nome.lower() == nome.lower():
                return u
        return None

    # -------- tarefas --------
    def criar_tarefa(self, titulo, prioridade):
        return Tarefa(titulo, prioridade)

    def atribuir_manual(self, nome_usuario, tarefa):
        usuario = self.encontrar_usuario(nome_usuario)

        if usuario:
            usuario.adicionar_tarefa(tarefa)
            print(f"Tarefa '{tarefa.titulo}' atribuída para {usuario.nome}")
        else:
            print("Usuário não encontrado.")

    def distribuir_automatico(self, tarefa):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        usuario = min(self.usuarios, key=lambda u: len(u.tarefas))
        usuario.adicionar_tarefa(tarefa)

        print(f"Tarefa '{tarefa.titulo}' atribuída automaticamente para {usuario.nome}")

    def listar_tarefas(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for u in self.usuarios:
            print(f"\n👤 {u.nome}")
            if not u.tarefas:
                print("  (sem tarefas)")
            for t in u.tarefas:
                print(f"  - {t}")


# ---------------- MENU ----------------

def menu():
    sistema = SistemaTarefas()

    while True:
        print("\n===== SISTEMA DE TAREFAS =====")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Criar e atribuir tarefa manual")
        print("4 - Criar e distribuir tarefa automática")
        print("5 - Listar tarefas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        # ---- criar usuário ----
        if opcao == "1":
            nome = input("Nome do usuário: ")
            sistema.adicionar_usuario(nome)

        # ---- listar usuários ----
        elif opcao == "2":
            sistema.listar_usuarios()

        # ---- manual ----
        elif opcao == "3":
            titulo = input("Título da tarefa: ")

            print("Prioridade: 1-BAIXA | 2-MÉDIA | 3-ALTA")
            p = input("Escolha: ")

            prioridade = {
                "1": Prioridade.BAIXA,
                "2": Prioridade.MEDIA,
                "3": Prioridade.ALTA
            }.get(p, Prioridade.BAIXA)

            usuario = input("Nome do usuário: ")

            tarefa = sistema.criar_tarefa(titulo, prioridade)
            sistema.atribuir_manual(usuario, tarefa)

        # ---- automático ----
        elif opcao == "4":
            titulo = input("Título da tarefa: ")

            print("Prioridade: 1-BAIXA | 2-MÉDIA | 3-ALTA")
            p = input("Escolha: ")

            prioridade = {
                "1": Prioridade.BAIXA,
                "2": Prioridade.MEDIA,
                "3": Prioridade.ALTA
            }.get(p, Prioridade.BAIXA)

            tarefa = sistema.criar_tarefa(titulo, prioridade)
            sistema.distribuir_automatico(tarefa)

        # ---- listar tarefas ----
        elif opcao == "5":
            sistema.listar_tarefas()

        # ---- sair ----
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


# ---------------- EXECUTAR ----------------

menu()