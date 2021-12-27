#include <stdio.h>

void move(int num_disk, int id_start_tray, int id_target_tray, int id_via_tray)
{
    //cnt_disk is number of disk and index
    //disk is indexed based on size; disk 0 is the most smallest one, disk n is the biggest
    //if there is only one disk, it is indexed disk '0'
    //start_tray is A and is indexed '1', target_tray is B and is indexed '2'

    int a=id_start_tray;
    int b=id_target_tray;
    int c=id_via_tray;//initiate variable

    if(num_disk==0)
    {
        //printf("\n-1 Period is over-\n");
        return;
    }

    move(num_disk-1, a, c, b);//disk 0~n-1 go to tray c from a
    printf("move disk %d from tray %d to tray %d\n",num_disk-1,a,b);
    move(num_disk-1, c, b, a);
}
int main()
{

    move(3,1,2,3);

    return 0;
}
