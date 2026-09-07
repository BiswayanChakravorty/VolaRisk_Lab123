import assert from 'node:assert/strict';
import test from 'node:test';
import {logReturns, annualizedVolatility, maxDrawdown, beta, garch, kalman} from '../app.js';

test('log returns match expected values',()=>assert.deepEqual(logReturns([100,110,121]).map(x=>Number(x.toFixed(6))),[0.09531,0.09531]));
test('risk metrics handle standard series',()=>{assert.equal(maxDrawdown([100,120,90,110]),-.25);assert.equal(beta([.02,-.04,.06,-.02],[.01,-.02,.03,-.01]),2);assert(annualizedVolatility([.01,-.02,.015])>0);assert.equal(garch([.01,-.02,.015]).length,3);assert.equal(kalman([.02,-.04,.06],[.01,-.02,.03]).length,3)});
test('invalid prices and zero variance are rejected',()=>{assert.throws(()=>logReturns([100,0,110]));assert.throws(()=>beta([.01,.02,.03],[.01,.01,.01]))});
