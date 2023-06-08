package org.ln.circlecicodecovgate;

public class UncoveredClass {
    public int isNineOrTenOrMaxValue(String input) {
        if (input.equals("nine")) {
            return 9;
        }

        if (input.equals("ten")) {
            return 10;
        }

        return Integer.MAX_VALUE;
    }
}
