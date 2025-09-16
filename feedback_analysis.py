def calculate_positive_feedback(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for r in ratings if r >= 4)
    return (positive_count / len(ratings)) * 100
def main():
    ratings_input = input("Enter ratings separated by commas ")
    ratings = []
    for r in ratings_input.split(','):
        r = r.strip()
        if r.isdigit():
            rating = int(r)
            if 1 <= rating <= 5:
                ratings.append(rating)
    if not ratings:
        print("No valid ratings entered.")
    else:
        percentage = calculate_positive_feedback(ratings)
        print(f"Positive Feedback: {percentage}%")
if __name__ == "__main__":
    main()
