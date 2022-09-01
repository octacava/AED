

#registro

class Venta():
    def __init__(self,num,importe_factura,tipo_factura,apellido,tipo_perfume):


        self.num = num
        self.importe_factura = importe_factura
        self.tipo_factura = tipo_factura
        self.apellido = apellido
        self.tipo_perfume = tipo_perfume

    def __str__(self):

        res= 'Numero factura: '+ str(self.num) + ' Importe de factura: ' + str(self.importe_factura) + \
             ' Tipo de factura: ' + str(self.tipo_factura) + ' Apellido: ' + str(self.apellido) + \
             ' Tipo de perfume: ' + str(self.tipo_perfume)
        return res
