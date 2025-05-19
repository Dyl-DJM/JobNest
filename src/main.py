def main():
    print("App is running but does nothing yet.")
    # Boucle infinie simple pour garder l'app "active"
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nApp stopped by user.")

if __name__ == '__main__':
    main()