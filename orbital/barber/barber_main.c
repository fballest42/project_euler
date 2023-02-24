#include"barber.h"

void error_message(int num_error)
{
	if (num_error == 1)
	{
		printf(RED);
		printf("SORRY YOUR NUMBER OF CHAIRS MUST BE BETWEEN 1 AND 9\n");
		printf(WHITE);	
	}
	else if (num_error == 2)
	{
		printf(RED);
		printf("SORRY YOUR NUMBER OF CUSTOMERS MUST BE BETWEEN 1 AND 999999\n");
		printf(WHITE);	
	}
	else if (num_error == 3)
	{
		printf(RED);
		printf("SORRY YOUR TIME MUST BE BETWEEN 50 AND 5000,\n");
		printf("BELOW 50 IT COULD BE UNSTABLE, AND UP 5000 IS GOING TO BE TOO SLOW\n");
		printf(WHITE);
	}
}

int check_numbers(char *intro)
{
	int i = 0;
	int x = 0;

	while (intro[i] != '\0')
	{
		if(isdigit(intro[i++]))
			x++;
		else
			return (0);
	}
	return (x);
}

char *valid_entry(char *question)
{
	char	*chars_set = NULL;
	bool	valid = false;
	size_t	size = 0;
	int		ret = 0;
	
	while (!valid)
	{
		printf("%s %s", "INSERT NUMBER OF", question);
		ret = getline(&chars_set, &size, stdin);
		chars_set[ret - 1] = '\0';
		if (check_numbers(chars_set) != 0)
			valid = true;
		else
		{
			free(chars_set);
			chars_set = NULL;
			size = 0;
			continue;
		}

	}

	return (chars_set);
}

int insert_options(t_data *data)
{
	char	*tmp;
	bool	valids = false;
	int 	i = 1;

	while (valids == false)
	{
		if (i == 1)
		{
			tmp = valid_entry("CHAIRS IN WAITING ROOM ? >>> ");
			data->chairs_num = atoi(tmp);
			free(tmp);
			if (data->chairs_num > 1 && data->chairs_num < 9)
				i = 2;
			else
				error_message(i);
		}
		if (i == 2)
		{
			tmp = valid_entry("CUSTOMERS OF THE JOURNEY ? >>> ");
			data->customer_num = atoi(tmp);
			free(tmp);
			if (data->customer_num > 1 && data->customer_num < 999999)
				i = 3;
			else
				error_message(i);
		}
		if (i == 3)
		{
			tmp = valid_entry("MILISECONDS FOR SETUP THE SHAVE TIME ? >>> ");
			data->time_shave = atoi(tmp);
			free(tmp);
			if (data->time_shave >= 50 && data->time_shave <= 5000)
				valids = true;
			else
				error_message(i);
		}
	}
	return (0);
}

void wellcome(t_data *data, int start_point)
{
	if (start_point == 1)
	{
		printf(YELLOW);
		printf("*******************************************************************\n");
		printf("*               WELLCONE TO THE PETE'S BARBER SHOP.               *\n");
		printf("*                   BEFORE TO START THE PROGRAM,                  *\n");
		printf("*      WE NEED SOME INFORMATION TO MAKE PETE WORKS PROPERLY       *\n");
		printf("*******************************************************************\n\n");
		printf(WHITE);
	}
	else if (start_point == 2)
	{
		printf(GREEN);
		printf("WELLDONE.\nNOW PETE THE BARBER IS GOING TO WORK WITH YOUR CHOICES:\n");
		printf("NUMBER OF CHAIRS IN WAITING ROOM ----------> %d\n", data->chairs_num);
		printf("NUMBER OF CUSTOMERS DURING THE JOURNEY ----> %d\n",data->customer_num);
		printf("THE SHAVING TIME FOR EACH CUSTOMER --------> %d\n", data->time_shave );
		printf(WHITE);
	}
}

int main()
{
	t_data	data;

	system("clear");
	wellcome(&data, 1);
	insert_options(&data);
	wellcome(&data, 2);

	return (0);
}

