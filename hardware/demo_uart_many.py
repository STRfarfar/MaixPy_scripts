from fpioa_manager import fm
from machine import UART
from board import board_info
from fpioa_manager import fm

# maixduino board_info PIN10/PIN11/PIN3/PIN4 or other hardware IO 4/11/10/3
fm.register(board_info.PIN10, fm.fpioa.UART1_TX, force=True)
fm.register(board_info.PIN11, fm.fpioa.UART1_RX, force=True)
fm.register(board_info.PIN3, fm.fpioa.UART2_TX, force=True)
fm.register(board_info.PIN4, fm.fpioa.UART2_RX, force=True)

uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

write_bytes = b'hello world'
for i in range(20):
    uart_A.write(write_bytes)

    read_data = uart_B.read()
    if read_data:
        read_str = read_data
        print("string = ", read_str)
        if read_str == write_bytes:
            print("baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully")


uart_A.deinit()
uart_B.deinit()
del uart_A
del uart_B

