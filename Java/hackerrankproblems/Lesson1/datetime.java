package Lesson1;

import java.util.*;
// import java.time.LocalDate;
// import java.time.format.DateTimeFormatter;

class Result {
    static List<String> days = Arrays.asList("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY");

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        Calendar c = Calendar.getInstance();
        c.set(year, month-1, day);
        int p = c.get(Calendar.DAY_OF_WEEK);
        String s = days.get(p-1);

        return s;

    }

}