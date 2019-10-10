#include "comm.h"
#include <stdint.h>
#include <stdbool.h>
#include "stm32f3xx_hal.h"

#define MAX_MSG_LENGTH 100

UART_HandleTypeDef huart2;
char msg[MAX_MSG_LENGTH];
uint8_t index;

void comm_init()
{
	index = 0;
}

void comm_do()
{

	char buffer[1];

	HAL_UART_Receive(&huart2, buffer, sizeof(buffer), HAL_MAX_DELAY);

	if(buffer[0] == '\n')
	{
		msg[index++] = buffer[0];

		HAL_UART_Transmit(&huart2, (uint8_t*)msg, index, 0xFFFF);
		index = 0;
	}
	else
	{
		msg[index++] = buffer[0];
	}

	if(index >= MAX_MSG_LENGTH)
	{
		index = 0; // no mercy for long messages!!!!
	}

}
