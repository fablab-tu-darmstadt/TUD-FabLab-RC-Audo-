#include "pwm.h"
#include "stm32f3xx_hal.h"

#include <stdio.h>
#include <string.h>

#define NEUTRAL 18450
#define MAX 18900
#define MIN 18050

#define FLYER_OPEN 1800
#define FLYER_CLOSED 560

#define GUMMI_OPEN 1890
#define GUMMI_CLOSED 920


uint16_t steering;
uint16_t motorlevel;
uint16_t flyer_value;
uint16_t gummi_value;

UART_HandleTypeDef huart2;









void pwm_init()
{
	steering = NEUTRAL;
	motorlevel = NEUTRAL;
	flyer_value = FLYER_CLOSED;
	gummi_value = GUMMI_CLOSED;

	//TIM3->CR1 |= TIM_CR1_CEN;

	TIM3->CCR1 = steering;
	TIM3->CCR2 = motorlevel;
	TIM3->CCR3 = flyer_value;
	TIM3->CCR4 = gummi_value;

}

void pwm_do()
{
	TIM3->CCR1 = steering;
	TIM3->CCR2 = motorlevel;
	TIM3->CCR3 = flyer_value;
	TIM3->CCR4 = gummi_value;
}

void set_steering(uint16_t steer)
{

	char msg[100];
	//if(steer >= MIN && steer <= MAX)
	//{
		steering = steer;
		sprintf(msg, "Set Steering to %i\n",steer);
		//}
		//else
		//{
		//	sprintf(msg, "Invalid value! %i to %i\n",MIN,MAX);
		//}
	//HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);

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
	//HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);

	//motorlevel = motor;
}


void set_flyer(uint16_t value)
{
	char msg[100];
	flyer_value = value;
	/*
	if(value > 0)
	{
		flyer_value = FLYER_OPEN;
		sprintf(msg, "Flyer box open");
	}
	else
	{
		flyer_value = FLYER_CLOSED;
		sprintf(msg, "Flyer box closed");
	}
	*/
	//HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);
}

void set_gummi(uint16_t value)
{
	char msg[100];
	gummi_value = value;
	/*
	if(value > 0)
	{
		gummi_value = GUMMI_OPEN;
		sprintf(msg, "Gummi box open");
	}
	else
	{
		gummi_value = GUMMI_CLOSED;
		sprintf(msg, "Gummi box closed");
	}
	*/
	//HAL_UART_Transmit(&huart2, (uint8_t*)msg, strlen(msg), 0xFFFF);
}








