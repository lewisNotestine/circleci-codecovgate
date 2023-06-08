package org.ln.circlecicodecovgate;

import junit.framework.TestCase;
import org.junit.Assert;

public class CoveredClassTest extends TestCase {

    private String mInput;
    private CoveredClass mTestSubject;
    private int mResult;

    @Override
    public void setUp() throws Exception {
        super.setUp();
        mTestSubject = new CoveredClass();
    }

    public void testOne() {
        // arrange
        givenInputIs("one");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(1, mResult);
    }

    public void testTwo() {
        // arrange
        givenInputIs("two");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(2, mResult);
    }

    public void testOther() {
        // arrange
        givenInputIs("notOneOrTwo");

        // act
        whenIsOneOrTwoOrMaxCalled();

        // assert
        Assert.assertEquals(Integer.MAX_VALUE, mResult);
    }

    private void givenInputIs(String input) {
        mInput = input;
    }

    private void whenIsOneOrTwoOrMaxCalled() {
        mResult = mTestSubject.isOneOrTwoOrMaxValue(mInput);
    }
}