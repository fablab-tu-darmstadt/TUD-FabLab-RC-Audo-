#include "comm.h"
#include <stdint.h>
#include <stdbool.h>
#include "stm32f3xx_hal.h"
#include <stdio.h>

#define MAX_MSG_LENGTH 100
#define MAXSPLITS 10

typedef struct SplittedStr_
{
    uint8_t cnt;
    char* strs[MAXSPLITS];
    bool completelySplitted;
} SplittedStr_t;


UART_HandleTypeDef huart2;
char msg[MAX_MSG_LENGTH];
uint8_t index;

void comm_init()
{
	index = 0;
}

void strsplit(SplittedStr_t* sstr,
                    char* str,
                    char splitchar,
                    char quotechar,
                    uint8_t maxsplits);

void parse()
{

	SplittedStr_t sstr;
	strsplit(&sstr, msg, ' ', '"', 10);

	char send[100];

	/*
	sprintf(send, "Splits = %i\n",sstr.cnt);

	HAL_UART_Transmit(&huart2, (uint8_t*)send, strlen(send), 0xFFFF);



	HAL_UART_Transmit(&huart2, (uint8_t*)sstr.strs[0], strlen(sstr.strs[0]), 0xFFFF);

	sprintf(send, "\n");
	HAL_UART_Transmit(&huart2, (uint8_t*)send, strlen(send), 0xFFFF);

	HAL_UART_Transmit(&huart2, (uint8_t*)sstr.strs[1], strlen(sstr.strs[1]), 0xFFFF);

	sprintf(send, "\n");
	HAL_UART_Transmit(&huart2, (uint8_t*)send, strlen(send), 0xFFFF);

	*/


	if(strcmp(sstr.strs[0], "Servo") == 0 && sstr.cnt == 2)
	{
		int servo = atoi(sstr.strs[1]);

		//char send[100];
		sprintf(send, "Servo = %i",servo);

		HAL_UART_Transmit(&huart2, (uint8_t*)send, strlen(send), 0xFFFF);

	}
}

void comm_do()
{

	char buffer[1];

	HAL_UART_Receive(&huart2, buffer, sizeof(buffer), HAL_MAX_DELAY);

	if(buffer[0] == '\n')
	{
		msg[index++] = buffer[0];

		HAL_UART_Transmit(&huart2, (uint8_t*)msg, index, 0xFFFF);
		parse();
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

void strsplit(SplittedStr_t* sstr,
                    char* str,
                    char splitchar,
                    char quotechar,
                    uint8_t maxsplits)
{
    uint16_t cnt = 0;
    bool bInStr = false;
    bool bInQuote = false;
    char C;
    char* pLastSplitPoint = 0;

    sstr->strs[0] = str;
    sstr->cnt = 0;
    sstr->completelySplitted = true;

    while(*str != '\0')
    {
        C = *str;

        if (bInQuote)
        {
            if (C == quotechar)
            {
                bInQuote = false;
            }
        }
        else if ( bInStr && (C == quotechar) )
        {
            bInQuote = true;
        }
        else if ( bInStr && (C == splitchar) )
        {
            *str = '\0';

            bInStr = false;

            pLastSplitPoint = str;
        }
        else if ( !bInStr && (C != splitchar) )
        {
            ++cnt;

            bInStr = true;

            if (cnt > maxsplits)
            {
                *pLastSplitPoint = splitchar;
                sstr->completelySplitted = false;
                sstr->cnt = maxsplits;
                return;
            }

            sstr->strs[cnt - 1] = str;

            if (C == quotechar)
            {
                bInQuote = true;
            }
        }

        ++str;
    }

    sstr->cnt = cnt;

    return;
}
