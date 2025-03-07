def decode_data(data):
    Dat = ''
    Dat += data[2]
    Dat += data[3]
    Dat += '/'
    Dat += data[0]
    Dat += data[1]
    return Dat

class Reserva:
    def __init__(self,d_inicio,d_final,cliente,num_quarto,__status):
        self.__data_inicio = d_inicio
        self.__data_final = d_final
        self.__cliente = cliente
        self.__num_quarto = num_quarto
        self.__status = __status

    def get_data_inicio(self):
        return self.__data_inicio
    
    def get_data_final(self):
        return self.__data_final
    
    def get_cliente(self):
        return self.__cliente
    
    def get_num_quarto(self):
        return self.__num_quarto
    
    def get_status(self):
        return self.__status
    
    def imprime_infos(self):
        __status = self.get_status()
        if __status == 'a':
            __status = 'Ativa'
        elif __status == 'c':
            __status = 'Cancelado'
        elif __status == 'i':
            __status = 'Check-In Feito'
        elif __status == 'o':
            __status = 'Check-Out Feito'
        print(f'Nome do Cliente: {self.get_cliente()}\nData de Início da Reserva: {decode_data(self.get_data_inicio())}\nData de Fim da Reserva: {decode_data(self.get_data_final())}\nNúmero do Quarto: {self.get_num_quarto()}\nStatus da Reserva: {__status}')
    
    def cancela_reserva(self):
        self.__status = 'c'
    
    def fazer_check_in(self):
        self.__status = 'i'
    
    def fazer_check_out(self):
        self.__status = 'o'
