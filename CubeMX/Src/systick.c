#include "systick.h"
#include <stdint.h>
#include <stdbool.h>
#include "stm32f3xx_hal.h"
#include "pwm.h"
#include <string.h>

UART_HandleTypeDef huart2;

uint32_t tick;

void systick_init()
{
	tick = 0;
}

void HAL_SYSTICK_Callback(void)
{
	tick++;
	pwm_do();

	if(tick == 1000)
	{
		tick = 0;

	}


}
