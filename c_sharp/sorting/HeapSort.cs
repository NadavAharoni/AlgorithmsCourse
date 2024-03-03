using System;

namespace sorting
{
    public class HeapSort
    {
        public static void MaxHeapify(List<int> list, int root)
        {
            int left = Left(root);
            int right = Right(root);

            Console.WriteLine($"root={root}, left={left}, right={right}, list length={list.Count}");

        }
 
        public static int Left(int i)
        {
            int left = 2 * i;
            return left; 
        }

        public static int Right(int i)
        {
            int right = 2 * i + 1;
            return right;
        }

    }
}