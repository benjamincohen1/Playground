import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.Date;

public class CodingPuzzle
{
public static List<Point> lAllPoints = new ArrayList<Point>();
public static int iMaxX;
public static int iMaxY;
public static int iCompletePaths = 0;

public static void depthFirstSearch(Point current, Stack<Point> result)
{
    if (result.contains(current))
        return;

    result.push(current);

    if (current.x == 1 && current.y == iMaxY && result.size() == iMaxX*iMaxY)
    {
        // This is a complete path
        iCompletePaths++;
    }
    for (Point p: getPossibleMoves(current))
    {
        depthFirstSearch(p, result);
    }

    // No path was found
    result.pop();
    return;
}

public static List<Point> getPossibleMoves (Point fromPoint)
{
    int iCurrentPointIndex = lAllPoints.indexOf(fromPoint);
    List<Point> lPossibleMoves = new ArrayList<Point>();

    if (fromPoint.x == 1 && fromPoint.y == 1)
    {
        // Top left point
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + iMaxY));
    }

    else if (fromPoint.x == 1 && fromPoint.y == iMaxY)
    {
        // Bottom left point. Should always be the last point. No valid moves.
        // If a path gets here before the end it shouldn't need to continue.
    }

    else if (fromPoint.x == iMaxX && fromPoint.y == 1)
    {
        // Top right point
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
    }

    else if (fromPoint.x == iMaxX && fromPoint.y == iMaxY)
    {
        // Bottom right point
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - 1));
    }

    else if (fromPoint.x == 1 && fromPoint.y != iMaxY)
    {
        // Any other point on the left side
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + iMaxY));
    }

    else if (fromPoint.x == iMaxX)
    {
        // Any other point on the right side
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
    }

    else if (fromPoint.y == 1)
    {
        // Any other point on the top
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + iMaxY));
    }

    else if (fromPoint.y == iMaxY && fromPoint.x != 1)
    {
        // Any other point on the bottom
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + iMaxY));
    }

    else
    {
        // Any other point not on an edge.
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - 1));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex - iMaxY));
        lPossibleMoves.add(lAllPoints.get(iCurrentPointIndex + iMaxY));
    }

    return lPossibleMoves;
}

public static void setUpGrid(int x, int y)
{
    iMaxX = x;
    iMaxY = y;
    for (int i = 1; i <= x; i++)
        for (int j = 1; j <= y; j++)
            lAllPoints.add(new Point(i, j));
}

public static void main(String[] args)
{
    Date start = new Date(System.currentTimeMillis());
    setUpGrid(10, 4);
    Stack<Point> sCurrentPoints = new Stack<Point>();
    depthFirstSearch(lAllPoints.get(0), sCurrentPoints);
    Date end = new Date(System.currentTimeMillis());
    long total = end.getTime() - start.getTime();
    System.out.println(iCompletePaths + " paths found in " + total/1000 + " seconds.");
}
}