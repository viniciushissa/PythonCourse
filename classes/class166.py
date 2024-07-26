from dataclasses import dataclass, asdict, astuple, field, fields

@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', repr=True
    )
    sobrenome: str = 'Not Sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    # print(asdict(p1))
    # print(astuple(p1))
    print(p1)
    # print(fields(p1))