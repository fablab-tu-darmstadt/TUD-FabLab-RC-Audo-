#ifndef __PWM_H
#define __PWM_H

#include <stdint.h>

void pwm_init();

void set_steering(uint16_t steer);

void set_motorlevel(uint16_t motor);

void set_flyer(uint16_t value);

void set_gummi(uint16_t value);

void pwm_do();







#endif
