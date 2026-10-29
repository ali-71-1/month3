# # import time

# # def task(name, seconds):
# #     print(f"Упала задача {name} начал работу!")
# #     time.sleep(seconds)
# #     print(f"Задача {name} готово!")


# # task("Задача 1", 4)
# # task("Задача 2", 2)
# # task("Задача 3", 3)


# import asyncio



# async def task(name, seconds):
#     print(f"Упала задача {name} начал работу!")
#     await asyncio.sleep(seconds)
#     print(f"Задача {name} готово!")


# async def main():
#     await asyncio.gather(
#         task("Задача 1", 4),
#         task("Задача 2", 2),
#         task("Задача 3", 3),
#     )

# asyncio.run(main())