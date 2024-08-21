from rayleigh import Rayleigh


def main():
    ray = Rayleigh()
    ray_i = ray.get_ray(0.1, 1, 45, 30, 90)
    print(ray_i)


if __name__ == "__main__":
    main()
