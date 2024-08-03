;; abs-value-cond :: Number -> Number
;; calcula el valor absoluto de x
(define (abs-value-cond x)
    (cond
        [(> x 0) x]
        [(= x 0) 0]
        [(< x 0) (- x)]))