;; solve-cuadratic-no-let :: Number Number Number -> Number
;; encuentra una solución real para ax^2+bx+c, si existe.
(define (solve-cuadratic-no-let a b c)
    (if (> (- (* b b) (* 4 a c)) 0)
        (+ (- b) (/ (sqrt (- (* b b) (* 4 a c))) (* 2 a)))
        (error "No real solution")))