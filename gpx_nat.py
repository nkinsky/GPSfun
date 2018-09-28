import numpy as np
import gpxpy
import gpxpy.gpx as gpx

def points2float(gpx_track):
    """
    takes all the points in a track and spits them out as a 2-d float
    :param gpx_track: track object from gpx.py
    :return: points: in float format
    """
    
    points = np.empty([gpx_track.get_points_no(), 2])
    n = 0
    for segment in gpx_track.segments:
        for point in segment.points:
            points[n, 0] = point.longitude
            points[n, 1] = point.latitude
            n = n + 1

    return points, n


if __name__ == '__main__':
    pos = get_pos('E:\\Eraser\\Marble7\\20180319_2_fcbox')
    pos_fix = fix_pos(pos)
    pass