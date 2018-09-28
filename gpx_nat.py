import numpy as np
import gpxpy
import gpxpy.gpx as gpx


def import_gpx(file):
    """Imports the GPX file and spits it out in gpx track format

    :param file: gpx file location
    :return: gpx_track
    """

    gpx_file = open(file, 'r')
    gpx_out = gpxpy.parse(gpx_file)

    return gpx_out


def points2float(gpx_track):
    """
    takes all the points in a track and spits them out as a 2-d float
    :param gpx_track: track object from gpx.py
    :return: points: in float format
            elevation: in float format
            n: number of points
    """
    
    points = np.empty([gpx_track.get_points_no(), 2])
    elevation = np.empty([gpx_track.get_points_no(), 1])
    n = 0
    for segment in gpx_track.segments:
        for point in segment.points:
            points[n, 0] = point.longitude
            points[n, 1] = point.latitude
            elevation[n] = point.elevation
            n = n + 1

    return points, elevation, n


def get_time_sec(gpx_track):
    """ Gets time in seconds of each point

    :param gpx_track:
    :return: time_in_sec: time in seconds from start, float
            start_time: absolute start time in datetime format
    """
    start_time = gpx_track.segments[0].points[0].time
    time_in_sec = np.empty([gpx_track.get_points_no(), 1])
    n = 1
    for segment in gpx_track.segments:
        for point in segment.points:
            curr_time = point.time
            time_in_sec[n] = curr_time - start_time
            n = n + 1

    return time_in_sec, start_time


def get_stopped_pts(gpx_track, speed_threshold=2.5):
    """Identifies times when stopped (below speed threshold) for GPX track.

    :param gpx_track:
    :param speed_threshold: in km/h (default = 2.5)
    :return: stopped_bool: boolean with True for points where stopped
            stopped_time: total time stopped
    """

    n = 0
    stopped_bool = [False]*gpx_track.get_points_no()  # pre-allocate
    for segment in gpx_track.segments:
        for ida, point in enumerate(segment.points):
            stopped_bool[n] = segment.get_speed[ida] < speed_threshold
            n = n + 1

    _, stopped_time = gpx_track.get_moving_data(speed_threshold)

    return stopped_bool, stopped_time


def calc_calories(gpx_track, wt = 175, activity='Run'):
    """Calculate calories burned based on weight and activity type (is that all I need)?

    :param gpx_track:
    :param wt: in lbs
    :param activity: 'Run' or 'Bike'
    :return:
    """



if __name__ == '__main__':
    pos = get_pos('E:\\Eraser\\Marble7\\20180319_2_fcbox')
    pos_fix = fix_pos(pos)
    pass