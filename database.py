import mysql.connector

class DataBase():
    def __init__(self, banco = "sysdark") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database=self.banco,user='root',password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor de Banco de Dados: ",db_info)
        else:
            print("Erro")  

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cadastro(
                id int not null auto_increment,
                cnpj varchar(50) not null,
                nome varchar(50) not null,
                fone char(12),
                email varchar(50),
                endereco varchar(50),
                cidade varchar(50),
                estado varchar(50),
                constraint primary key (id)
                );
            """)

        except Exception as err:
            print(err)

    def select(self):
        self.connect()
        try:
            self.cursor.execute("""
                SELECT * FROM cadastro ORDER BY ID DESC;
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            #for linha in result:
            #   print(linha)
            
            return result
            #retorn a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def filter(self,texto):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM cadastro WHERE nome LIKE '%{texto}%' or cnpj LIKE '%{texto}%';
            """)
            result = self.cursor.fetchall()
            
            #verifica os dados do select
            for linha in result:
               print(linha)
            
            return result
            #retorna a lista do banco para quem chamou a função
        except Exception as err:
            print(err)

        finally:
            self.close_connection()


    def insert(self,cnpj,nome,fone,email,endereco,cidade,estado):
        self.connect()
        try:
            self.cursor.execute("""
                INSERT INTO cadastro (cnpj,nome,fone,email,endereco,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s,%s)
            """,(cnpj,nome,fone,email,endereco,cidade,estado))
            self.conn.commit()
            return "OK","Cadastro realizado com sucesso!!"

        except Exception as err:
            #print(err)
            return "ERRO",str(err)

        finally:
            self.close_connection()
   
    def update(self,tupla_de_dados):
        #print(tupla_de_dados)
        self.connect()
        try:
                self.cursor.execute(f"""UPDATE cadastro SET 
                cnpj = '{tupla_de_dados[1]}',
                nome = '{tupla_de_dados[2]}',
                fone = '{tupla_de_dados[3]}',
                email = '{tupla_de_dados[4]}',
                endereco = '{tupla_de_dados[5]}',
                cidade = '{tupla_de_dados[6]}'
                WHERE id={tupla_de_dados[0]}
                """)
                self.conn.commit()
                #quando o dado for string deve ter '{var}' se for inteiro somente {id}
                return 'OK','Dados atualizados com sucesso!!!'

        except AttributeError as err:
            print(err)
        
        finally:
            self.close_connection()


    def delete(self,id):
        self.connect()
        try:
            #self.connect()
            self.cursor.execute(
                f"""DELETE FROM cadastro WHERE id = '{id}' """
            )
            self.conn.commit()

            return "OK","Cadastro excluído com sucesso!"

        except Exception as err:
            print(err)
        
        finally:
            self.close_connection()


    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!")

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    #db.create_table()
    #db.insert("43434343","BLABLABLA","909090","bla@gmail.com","rua tal","CG","MS")
    #db.delete(23)
    #db.update(20,"PEDROO SAMPAIO SILVA")
    #dados = db.select()
    db.filter("444")
    db.close_connection()

