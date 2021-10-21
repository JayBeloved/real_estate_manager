from .models import Houses, Community
import random
import string

all_communities = Community.objects.all()


def geninsert(all_comm):
    already_existing = 0
    new_addition = 0
    for comm in all_comm:
        # Generator
        if comm.communitytype.housetype.is_block:
            if comm.communitytype.housetype.is_flat:
                # With Flats
                # get number of blocks
                block_count = comm.communitytype.housetype.block_count
                b_num = 0
                for block in range(1, block_count + 1):
                    b_num += 1
                    b_code = f"BL{b_num}"
                    # get number of flats
                    flat_count = comm.communitytype.housetype.flat_count
                    f_num = 0
                    f_code = None
                    for flat in range(1, flat_count + 1):
                        f_num += 1
                        f_code = f"FT{f_num}"
                        h_code = f"{comm.commcode}/{b_code}/{f_code}"

                        if Houses.objects.filter(housecode__contains=h_code).exists():
                            already_existing += 1
                        else:
                            new_addition += 1
            else:
                # Without Flats
                # get number of blocks
                block_count = comm.communitytype.housetype.block_count
                b_num = 0
                for block in range(1, block_count + 1):
                    b_num += 1
                    b_code = f"BL{b_num}"
                    # Randomly Choose Letters for adding to code
                    char1 = random.choice(string.ascii_uppercase)
                    char2 = random.choice(string.ascii_lowercase)
                    char3 = random.choice(string.ascii_letters)
                    char4 = random.choice('123456789')
                    ##########################
                    if Houses.objects.filter(housecode__contains=f'{comm.commcode}'):
                        already_existing += 1
                    else:
                        new_addition += 1

    print(f"New Added Houses: {new_addition} ")
    print(f"Already Existing Houses: {already_existing} ")


def NoFlats(all_comm):
    no_flats = 0
    for comm in all_comm:
        if comm.communitytype.housetype.is_block:
            if comm.communitytype.housetype.is_flat:
                pass
            else:
                tot_houses = Houses.objects.filter(housecode__contains=comm.commcode)
                for house in tot_houses:
                    no_flats += 1

    print(f'Total Number of Houses Without Flats : {no_flats}')


def DropFlats(all_comm):
    no_flats = 0
    for comm in all_comm:
        if comm.communitytype.housetype.is_block:
            if comm.communitytype.housetype.is_flat:
                pass
            else:
                tot_houses = Houses.objects.filter(housecode__contains=comm.commcode)
                for house in tot_houses:
                    house.delete()
                    no_flats += 1

    print(f'Total Number of Houses Deleted Houses : {no_flats}')
