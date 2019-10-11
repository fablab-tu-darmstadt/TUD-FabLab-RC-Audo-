#include "pwm.h"
#include "stm32f3xx_hal.h"

#include <stdio.h>
#include <string.h>

#define NEUTRAL 18450
#define MAX 18900
#define MIN 18050

uint16_t steering;
uint16_t motorlevel;
UART_HandleTypeDef huart2;









void pwm_init()
{
	steering = NEUTRAL;
	motorlevel = NEUTRAL;



	//TIM3->CR1 |= TIM_CR1_CEN;

	TIM3->CCR1 = steering;
	TIM3->CCR2 = motorlevel;


}

void pwm_do()
{
	TIM3->CCR1 = steering;
	TIM3->CCR2 = motorlevel;
}

void set_steering(uint16_t steer)
{

	char msg[100];
	if(steer >= MIN && steer <= MAX)
	{
		steering = steer;
		sprintf(msg, "Set Steering to %i\n",steer);
	}
	else
	{
		sprintf(msg, "Invalid value! %i to %i\n",MIN,MAX);
	}
	HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);

	//steering = steer;
}

void set_motorlevel(uint16_t motor)
{

	char msg[100];
	if(motor >= MIN && motor <= MAX)
	{
		motorlevel = motor;
		sprintf(msg, "Set Motorlevel to %i\n",motor);
	}
	else
	{
		sprintf(msg, "Invalid value! %i to %i\n",MIN,MAX);
	}
	HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);

	//motorlevel = motor;
}











