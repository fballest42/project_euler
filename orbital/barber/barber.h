#ifndef BARBER_H
# define BARBER_H

# include <unistd.h>
# include <stdio.h>
# include <ctype.h>
# include <limits.h>
# include <strings.h>
# include <stdbool.h>
# include <stdlib.h>
# include <fcntl.h>
# include <errno.h>
# include <pthread.h>
# include <sys/stat.h>
# include <time.h>
# include <sys/time.h>


# define WELLCOME "WELLCOME TO THE BARBER SHOP PROBLEM.\nBEFORE TO OPEN THE BARBER SHOP,\nWE NEED SOME INFORMATION.\n"
typedef struct s_customer
{
	int				num;
	int				meals;
	unsigned long	last_eat;
	pthread_t		thread;
	pthread_mutex_t	*shaving;
	struct s_data	*dp;
}				t_customer;

typedef struct s_data
{
	long			customer_num;
	long			chairs_num;
	int				shaving;
	int				time_shave;
	int				sleep;
	int				shaved;
	unsigned long	init_time;
	unsigned long	current_time;
	t_customer		*customer;
	pthread_mutex_t	*chairs;
	pthread_mutex_t	printer;
}				t_data;

#endif
