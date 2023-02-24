#include"barber.h"

int check_numbers(char *intro, int size)
{
	int i = 0;
	while (intro[i] != '\0' && intro[i] != '\n' && i < size)
	{
		if (isdigit(intro[i]))
			i++;
		else
			return (0);
	}
	return (i);
}

char *valid_entry(int size, char *question)
{
	char	*chars_set;
	bool	valid = false;
	int		ret = 0;
	int		size_m = 0;
	
	chars_set = calloc(size, sizeof(char));
	while (!valid)
	{
		printf("%s %s", "INSERT NUMBER OF", question);
		fgets(chars_set, size, stdin);
		size_m = strlen(chars_set);
		printf("SIZE_M=%d *** CHARS_SET = %s\n", size_m, chars_set);
		if (size >= size_m && check_numbers(chars_set, size))
			valid = true;
		else
		{
			free(chars_set);
			chars_set = calloc(size, sizeof(char));
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
			tmp = valid_entry(3, "CHAIRS IN WAITING ROOM ? >>> ");
			data->chairs_num = atol(tmp);
			free(tmp);
			if (data->chairs_num > 1 && data->chairs_num < 9)
				i = 2;
			else
				printf("SORRY YOUR NUMBER OF CHAIRS MUST BE BETWEEN 1 AND 9");
		}
		if (i == 2)
		{
			tmp = valid_entry(12, "CUSTOMERS OF THE JOURNEY ? >>> ");
			data->customer_num = atol(tmp);
			free(tmp);
			if (data->customer_num > 1 && data->customer_num < INT_MAX)
				i = 3;
			else
				printf("SORRY YOUR NUMBER OF CUSTOMERS MUST BE BETWEEN 1 AND MAX INTEGER");
		}
		if (i == 3)
		{
			tmp = valid_entry(12, "CUSTOMERS OF THE JOURNEY ? >>> ");
			data->customer_num = atol(tmp);
			free(tmp);
			if (data->customer_num > 1 && data->customer_num < INT_MAX)
				i = 3;
			else
				printf("SORRY YOUR NUMBER OF CUSTOMERS MUST BE BETWEEN 1 AND MAX INTEGER");
		}
	}
	return (0);
}

void wellcome(int start_point)
{
	if (start_point == 1)
	{
		printf("WELLCONE TO THE PETE'S BARBER SHOP.\n");
		printf("BEFORE TO START THE PROGRAM,\nWE NEED SOME INFORMATION TO MAKE PETE WORKS PROPERLY");
		printf("\n*************************************************\n\n");
	}
	else (startpoint == 2)
	{
		printf("WELLDONE.\nNOW PETE THE BARBER IS GOING TO WORK WITH YOUR CHOICE:\n");
		printf("NUMBER OF CHAIRS IN WAITING ROOM ----------> %ld\n", data->chairs_num);
		printf("NUMBER OF CUSTOMERS DURING THE JOURNEY ----> %ld\n",data->customer_num);
		printf("TIME SHAVING EACH CUSTOMER %d MILISECONDS\n", data.);
	}
}

int main()
{
	t_data	data;

	system("clear");
	wellcome(1);
	insert_options(&data);

	return (0);
}

