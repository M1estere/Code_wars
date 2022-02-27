public static class TimeFormat
{
    public static string GetReadableTime(int seconds)
    {
        if (seconds < 0 || seconds > 359999) return "99:59:59";
        if (seconds == 0) return "00:00:00";

        int hours = 0;
        int minutes = 0;
            
        if (seconds >= 3600)
        {
            hours = seconds / 3600;
            minutes = (seconds / 60) % 60;
            seconds = seconds - (hours * 3600) - (minutes * 60);
        } else
        {
            hours = 0;

            if (seconds >= 60)
            {
                minutes = (seconds / 60) % 60;
                seconds = seconds - (minutes * 60);
            } else
            {
                minutes = 0;
            }
        }

        string stringHours = "";
        string stringMinutes = "";
        string stringSeconds = "";

        if (hours < 10)
            stringHours = '0' + hours.ToString();
        else
            stringHours = hours.ToString();    
            
        if (minutes < 10)
            stringMinutes = '0' + minutes.ToString();
        else
            stringMinutes = minutes.ToString();

        if (seconds < 10)
            stringSeconds = '0' + seconds.ToString();
        else
            stringSeconds = seconds.ToString();    
            
        return stringHours + ":" + stringMinutes + ":" + stringSeconds;
    }
}