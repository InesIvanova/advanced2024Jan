def gather_credits(number_of_credits_needed, *course_info):
    courses_enrolled = {}

    for course_name, credits in course_info:
        if sum(courses_enrolled.values()) >= number_of_credits_needed:
            break

        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = credits

    if sum(courses_enrolled.values()) >= number_of_credits_needed:
        return (f"Enrollment finished! Maximum credits: {sum(courses_enrolled.values())}.\n"
                f"Courses: {', '.join(sorted(courses_enrolled))}")
    return (f"You need to enroll in more courses! "
            f"You have to gather {number_of_credits_needed - sum(courses_enrolled.values())} credits more.")


print(gather_credits(
    80,
    ("Basics", 27),
))


