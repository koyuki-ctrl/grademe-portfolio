#include <unistd.h>

int	main(int argc, char **argv)
{
	(void)argc;
	(void)argv;

	char i;

	i = 57;

	while (i >= 48)
	{
		write(1,&i,1);
		i--;
	}
	write(1,"\n",1);
	return (0);
}
