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

/* COLOURS DEFINITION TO USE IN OUTPUTS */
# define RED "\033[0;31m" 
# define GREEN "\033[0;32m"
# define BLUE "\033[0;34m"
# define YELLOW "\033[0;33m"
# define WHITE "\033[0;37m"

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
	int				customer_num;
	int				chairs_num;
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

/* FUNTIONS IN BARBER_MAIN.C FILE */
int		check_numbers(char *intro);
char 	*valid_entry(char *question);
int 	insert_options(t_data *data);
void 	wellcome(t_data *data, int start_point);

#endif
