package org.ln.circlecicodecovgate;

import junit.framework.TestCase;
import org.junit.Assert;

public class UncoveredClassTest extends TestCase {


    private String mInput;
    private UncoveredClass mTestSubject;
    private int mResult;

    public void setUp() throws Exception {
        super.setUp();

        mTestSubject = new UncoveredClass();
    }

    public void testIsNineOrTenOrMaxValue_nine() {
        // arrange
        givenInputIs("nine");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(9, mResult);
    }

    public void testIsNineOrTenOrMaxValue_ten() {
        // arrange
        givenInputIs("ten");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(10, mResult);
    }

    public void testIsNineOrTenOrMaxValue_max() {
        // arrange
        givenInputIs("notNineOrTen");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(Integer.MAX_VALUE, mResult);
    }
    private void givenInputIs(String input) {
        mInput = input;
    }

    private void whenIsOneOrTwoOrMaxCalled() {
        mResult = mTestSubject.isNineOrTenOrMaxValue(mInput);
    }
}