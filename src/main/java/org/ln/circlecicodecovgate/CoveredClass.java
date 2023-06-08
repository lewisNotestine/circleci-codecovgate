package org.ln.circlecicodecovgate;

public class CoveredClass {

    public int isOneOrTwoOrMaxValue(String input) {
        if (input.equals("one")) {
            return 1;
        }

        if (input.equals("two")) {
            return 2;
        }

        return Integer.MAX_VALUE;
    }
}
