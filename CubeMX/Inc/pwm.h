#ifndef __PWM_H
#define __PWM_H

#include <stdint.h>

void pwm_init();

void set_steering(uint16_t steer);

void set_motorlevel(uint16_t motor);

void pwm_do();







#endif
